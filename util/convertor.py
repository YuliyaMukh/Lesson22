from model.human import Human
class Convertor:

    @staticmethod
    def convert_to_string(humans):
        if not isinstance(humans, (list, tuple)):
            return "List is empty"

        s = "List is empty"

        for human in humans:
            if isinstance(human, Human):
                s += "\n" + str(human)

        return s