
def test_drodown_7235(py):
    py.visit("http://72-35.ru")
    py.get("[name='categoryID']").select('Пожалуйста, выберите')
    py.get("[name='param_23']").select('Aeroplast')
    pass
