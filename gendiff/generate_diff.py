def generate_diff(first_file, second_file):
    result = {}

    for key in first_file:
        if key in second_file and second_file[key] == first_file[key]:
            result['  ' + key] = first_file[key]
        elif key in second_file and second_file[key] != first_file[key]:
            result['- ' + key] = first_file[key]
            result['+ ' + key] = second_file[key]
        else:
            result['- ' + key] = first_file[key]

    for key in second_file:
        if key not in first_file:
            result['+ ' + key] = second_file[key]

    result = dict(sorted(result.items(), key=lambda x: x[0][2]))

    print('{')
    for key in result:
        print(' ', key, ':', result[key])
    print('}')

    return result
