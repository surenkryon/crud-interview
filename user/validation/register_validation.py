import gladiator as gl


def validate_request(request):
    field_validations = (
        ('mail_id', gl.format_email),
        ('first_name', gl.required),
        ('age', gl.gte(18)),
    )
    result = gl.validate(field_validations, request)

    # listing errors
    result_error_list = result._error_list()

    output = dict(result_error_list)

    return output
