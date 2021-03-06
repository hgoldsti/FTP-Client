def response_to_port_tuple(response):
    host_address = response[response.find('(') + 1:]
    host_address = host_address.replace(')', '')
    info_array = host_address.split(',')

    host_name = info_array[0] + '.' + \
                info_array[1] + '.' + \
                info_array[2] + '.' + \
                info_array[3]
    port_number = ((int(info_array[4])) * 256) + int(info_array[5])

    return (host_name, port_number)


def get_response(socket_file, command=None):
    if command:
        socket_file.write(command)
        socket_file.flush()
    while True:
        line = socket_file.readline()
        if line[0].isdigit() and line[1].isdigit and line[2].isdigit and line[
            3] == " ":
            return line


def get_retr_response(created_file):
    string_buffer = ''
    while True:
        new_line = created_file.readline()
        if not new_line:
            return string_buffer
        string_buffer += new_line
    return string_buffer
