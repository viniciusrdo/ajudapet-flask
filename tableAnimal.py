from flask_table import Table, Col, LinkCol


class Results(Table):
        animal_id = Col('animal_Id', show=False)
        animal_name = Col('animal_Name')
        animal_rescue_date = Col('animal_rescue_date')
        animal_gender = Col('animal_Gender')
        edit = LinkCol('Edit', 'edit_animal_view', url_kwargs=dict(id='animal_id'))
        delete = LinkCol('Delete', 'delete_animal', url_kwargs=dict(id='animal_id'))