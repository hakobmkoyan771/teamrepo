#!/usr/bin/python3

def generatorHtml(user_list):
    head = """<!DOCTYPE html>
            <html>
            <head>
                <style>
                    table, th, td {
                      border: 1px solid black;
                    }
                </style>
                <title>Users List</title>
            </head>"""

    body = """<body>
              <table>
                  <tr>
                    <td>Mail</td>
                    <td>Name</td>
                    <td>Surname</td>
                  </tr>"""
    for i in range(0, len(user_list), 3):
        body += """<tr>"""
        body += """<td>""" + str(user_list[i]) + """</td>"""
        body += """<td>""" + str(user_list[i+1]) + """</td>"""
        body += """<td>""" + str(user_list[i+2]) + """</td>"""

    body += """</table> 
                </body>
                </html>"""

    indexfile = head + body

    with open("templates/users.html", "w") as htmlfile:
        htmlfile.write(indexfile)


def users_on_html(users_list):
    ulist = []
    for i in users_list:
        for k, v in i.items():
            if k != "_id":
                ulist.append(v)
    generatorHtml(ulist)
