

class Behavior:

    def __init__(self, motors=None, val=None):
        """

        :param motors: En liste med motorene som motob-en skal bestemme instillinger på
        :param val: En mellomlagring for den siste motorandbefalingen sendt til motob-en
        """
        self.motors = motors
        self.value = val

    def update(self, n_m_recommendation):
        """
        Metode som oppdaterer motorandbefalingen
        :param n_m_recommendation: Tar inn en ny motor andbefaling
        :return:
        """
        self.value = new_motor_recommendation
        self.operationalize()

    def operationalize(self):
