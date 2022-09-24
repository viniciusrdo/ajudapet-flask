from flask_table import Table, Col, LinkCol


class Results(Table):
        donator_id = Col('donator_id', show=False)
        donator_name = Col('donator_name')
        donator_document = Col('donator_document')
        donator_email = Col('donator_email')
        # edit = LinkCol('Edit', 'edit_animal', url_kwargs=dict(id='animal_id'))
        # delete = LinkCol('Delete', 'delete_animal', url_kwargs=dict(id='animal_id'))