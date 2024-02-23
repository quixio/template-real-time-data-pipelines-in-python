from typing import Optional, Dict, Any
import os
import logging

from quixstreams.app import Application

logger = logging.getLogger()


class ProducerWrapper:
    """
    Wrapper around the quixstreams.kafka.Producer class, to handle both
    scenarios of
    - using local Kafka cluster or
    - Quix Kafka cluster.
    """

    def __init__(
        self,
        kafka_topic: str,
        use_local_kafka: Optional[bool] = False,
    ):

        if use_local_kafka:

            logger.info("Connecting to Local Kafka cluster...")

            app = Application(
                broker_address=os.environ["KAFKA_BROKER_ADDRESS"],
                consumer_group="ignored",
            )

            self._kafka_topic = app.topic(kafka_topic)

        else:
            logger.info("Connecting to Quix Kafka cluster...")

            app = Application.Quix(consumer_group="ignored")

            self._kafka_topic = app.topic(kafka_topic)

            # self._serialize = QuixTimeseriesSerializer()

        # calling get_producer() also creates any Application-generated topics.
        self._producer = app.get_producer()

    def produce(
            self,
            key,
            value: Dict[str, Any],
            headers=None,
            partition=None,
            timestamp=None
    ):
        serialized = self._kafka_topic.serialize(key=key, value=value, headers=headers)
        self._producer.produce(
            topic=self._kafka_topic.name,
            headers=serialized.headers,
            key=serialized.key,
            value=serialized.value,
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._producer.__exit__(exc_type, exc_value, traceback)