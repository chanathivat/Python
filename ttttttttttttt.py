class ChoicesCls():
    def __init__(self):
        self.OPTION_ONE = 'O1'
        self.OPTION_ONE_SHORT = 'Opt 1'
        self.OPTION_ONE_LONG = 'Option 1'
        self.OPTION_TWO = 'O2'
        self.OPTION_TWO_SHORT = 'Opt 2'
        self.OPTION_TWO_LONG = 'Option 2'

    def get_choices(self):
        return (
            (self.OPTION_ONE, self.OPTION_ONE_LONG),
            (self.OPTION_TWO, self.OPTION_TWO_LONG)
        )


class TestModel(models.Model):
    choices_obj = ChoicesCls()
    field = models.CharField(choices=choices_obj.get_choices)