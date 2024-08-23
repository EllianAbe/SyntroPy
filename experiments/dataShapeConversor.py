def convert_dict(input_dict, example_dict, path=[]):
    output_dict = {}

    for key, value in example_dict.items():
        if isinstance(value, dict):
            convert_dict(input_dict, value, path + [key])
            continue

        if isinstance(value, list):
            output_dict[key] = [convert_dict(input_dict, value[0], path + [key])
                                for element in nested_by_path(input_dict, path + [key])]
            continue

        if key in input_dict:
            output_dict[key] = nested_by_path(input_dict, path + [key])
            continue

        output_dict[key] = None

    return output_dict


def nested_by_path(data: dict, path=[]):
    if not path or not isinstance(data, dict):
        return data

    return nested_by_path(data.get(path[0]), path[1:])


    # Example usage:
input_dict = {
    'country': 'USA',
    'city': 'New York',
    'items': [
        {
            'product': 'Apple'
        },
        {
            'product': 'Orange'
        },
        {
            'product': 'Banana'
        }

    ]


}

example_dict = {
    'country': '',
    'items': [
        {
            'country': '',
            'city': '',
            'product': ''
        }
    ]
}


output = convert_dict(input_dict, example_dict)

print(output)
