from flask_table import Table, Col, LinkCol


# Nesta classe definimos o objeto "Adopter" proveniente da tabela do banco de dados.

class Results(Table):
        adopter_id = Col('adopter_id', show=False)
        adopter_name = Col('adopter_name')
        adopter_document = Col('adopter_document')
        adopter_email = Col('adopter_email')
        # edit = LinkCol('Edit', 'edit_animal', url_kwargs=dict(id='animal_id'))
        delete = LinkCol('Delete', 'delete_adopter', url_kwargs=dict(id='adopter_id'))
