import datetime
import time
from abc import ABC, abstractmethod

from google.protobuf.message import Message
from protovalidate import validate
from protovalidate.validator import ValidationError

from examples.common.zenoh_transmitter import create_zenoh_session


class ExamplePub(ABC):
    def __init__(self, key: str, hz: float | None) -> None:
        if hz and hz <= 0:
            raise ValueError("hz must be a non-negative number")

        self.session = create_zenoh_session()
        self.publisher = self.session.declare_publisher(key)
        self.hz = hz

    def run(self) -> None:
        try:
            while True:
                msg = self.create_message()

                # Validate the message before publishing
                try:
                    validate(msg)
                except ValidationError as e:
                    print(f"Validation failed: {e}")
                    if hasattr(e, "violations"):
                        print("Violations:", e.violations)
                    raise

                print(
                    f"[{datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]}] Publishing : {self.publisher.key_expr}: {msg}"
                )

                payload = msg.SerializeToString()

                self.publisher.put(payload)
                if self.hz is None:
                    break
                elif self.hz:
                    time.sleep(1.0 / self.hz)
                else:
                    print(
                        f"Error: hz must be a positive number, but got {self.hz}. Exiting."
                    )
                    break
        except KeyboardInterrupt:
            pass
        finally:
            self.session.close()  # type: ignore

    @abstractmethod
    def create_message(self) -> Message:
        pass
