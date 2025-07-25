from smells.QuantumSmell import QuantumSmell

class NC(QuantumSmell):
    def __init__(self, run_calls=None, assign_parameter_calls=None, explanation=None, suggestion=None):
        super().__init__("NC", row=None, column_start=None, column_end=None, explanation=explanation, suggestion=suggestion)
        self.run_calls = run_calls if run_calls else {}
        self.assign_parameter_calls = assign_parameter_calls if assign_parameter_calls else {}
        self.run_count = len(self.run_calls)
        self.bind_count = len(self.assign_parameter_calls)

    def update_explanation(self, explanation):
        self.set_explanation(explanation)

    def update_suggestion(self, suggestion):
        self.set_suggestion(suggestion)

    def as_dict(self):
        base = super().as_dict()
        base.update({
            'run_count': self.run_count,
            'assign_parameters_count': self.bind_count,
            'run_calls': self.run_calls,
            'assign_parameter_calls': self.assign_parameter_calls
        })
        return base
