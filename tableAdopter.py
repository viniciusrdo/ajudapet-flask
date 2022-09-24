from flask_table import Table, Col, LinkCol


class Results(Table):
        adopter_id = Col('adopter_id', show=False)
        adopter_name = Col('adopter_name')
        adopter_document = Col('adopter_document')
        adopter_email = Col('adopter_email')
        # edit = LinkCol('Edit', 'edit_animal', url_kwargs=dict(id='animal_id'))
        delete = LinkCol('Delete', 'delete_adopter', url_kwargs=dict(id='adopter_id'))