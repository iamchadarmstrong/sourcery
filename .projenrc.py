from projen.python import PythonProject

project = PythonProject(
    author_email="chad@armstrong.tech",
    author_name="iamchadarmstrong",
    module_name="sourcery_hack",
    name="sourcery-hack",
    poetry=True,
    python_exec="python3",
    version="0.1.0",
)

project.synth()