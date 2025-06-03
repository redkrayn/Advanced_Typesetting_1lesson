from livereload import Server, shell


server = Server()
server.watch("*.html", shell("make html", cwd=""))
server.serve(root='.')
