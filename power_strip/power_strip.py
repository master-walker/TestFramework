from abc import abstractmethod
from network.remote_system import RemoteSystem


class PowerStrip(RemoteSystem):
    """
    This class provides the Interface for the basic functions to manage the power strip.
    """

    @abstractmethod
    def port_status(self, port_id) -> str:
        """
        returns the status of the requested port

        :param port_id: port to be checked
        :return: command to query port status
        """
        pass

    @abstractmethod
    def create_command(self, port_id: int, on_or_off: bool) -> str:
        """
        generates the command to set the selected port to up or down

        :param port_id: port to be set
        :param on_or_off: turn on or off
        :return: command as string
        """
        pass