import json
import pydash as _

from data.constants import NAMES_MAP


def _get_or_create(session, model, **kwargs):

    instance = session.query(model).filter_by(**kwargs).first()

    if not instance:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()

    return instance


def manipulate_with_data_from_sheet_and_db(session, model, schema, query, data) -> None:
    db_data = schema.dump(query)
    gs_data_raw = json.dumps(
                        data,
                        sort_keys=False,
                        indent=4,
                        ensure_ascii=False,
                        separators=(',', ': '))
    gs_data_raw = json.loads(gs_data_raw)
    gs_data = []
    # print(type(gs_data_raw), "gs")

    for el in gs_data_raw[1:]:
        temp_obj = {}
        for value in el:
            key = gs_data_raw[0][el.index(value)]
            # print(key)
            temp_obj[NAMES_MAP[key]] = value
        gs_data.append(temp_obj)
        _get_or_create(session, model, **temp_obj)

    for el in db_data:
        if not _.find(gs_data, lambda o: o['order_num'] == el.get('order_num')):
            db_obj = model.query.get(el.get('id'))
            session.delete(db_obj)
            session.commit()

    # return db_data


# def _parse_list_to_json(data: list) -> list:
#     gs_data = []
#
#     for el in data[1:]:
#         temp_obj = {}
#         for value in el:
#             key = data[0][el.index(value)]
#             temp_obj[NAMES_MAP[key]] = value
#         gs_data.append(temp_obj)
#     return gs_data