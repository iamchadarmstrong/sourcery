from projen.python import PythonProject

project = PythonProject(
    author_email="chad@armstrong.tech",
    author_name="iamchadarmstrong",
    module_name="sourcery",
    name="sourcery",
    poetry=True,
    version="0.1.0",
)

project.synth()