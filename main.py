import random
from jinja2 import Template


def main():
    templatePath = "html/template/test-template.html"
    templateFile = open(templatePath)
    # read the template content as string
    templateContent = templateFile.read()
    templateFile.close()

    # load the string using jinja2 Template
    loadedTemplate = Template(templateContent)
    # place holder for data
    tableData = []

    colors = [
        "bg-primary",
        "bg-secondary",
        "bg-success",
        "bg-danger",
        "bg-warning",
        "bg-info",
        "bg-light",
        "bg-dark",
        "bg-white",
    ]

    count = 0
    for row in range(0, 7):
        columnData = []
        for col in range(0, 7):
            columnData.append({
                "data": count,
                "color": colors[random.randrange(0, 9)]
            })
            count = count + 1
        tableData.append(columnData)

    # generated static html is stored in dist directory
    # create a static html file to write to
    staticHtml = open("html/dist/static.html", "w")
    # get the rendered html
    # name, message, tableData are variable passed to the template
    # any number of variables can be passed to the template
    renderedHtml = loadedTemplate.render(
        name="bug", message="hello", tableData=tableData
    )
    # write the rendered html to file
    staticHtml.write(renderedHtml)
    staticHtml.close()


main()
