from projen.python import PythonProject
from projen import (
    License,
    vscode,
    DevEnvironmentDockerImage,
    Task,
)

project = PythonProject(
    author_email="chad@armstrong.tech",
    author_name="iamchadarmstrong",
    module_name="sourcery",
    name="sourcery",
    dev_deps=["sourcery_cli", "black"],
    poetry=True,
    python_exec="python",
    version="0.1.0",
    github=True,
    vscode=True,
    github_options={"pull_request_lint": True},
)
License(project=project, spdx="WTFPL")
devContainer = vscode.DevContainer(project=project)
devContainer.add_docker_image(
    DevEnvironmentDockerImage.from_image("mcr.microsoft.com/devcontainers/base:jammy")
)
devContainer.add_vscode_extensions("sourcery.sourcery")
devContainer.add_features(
    vscode.DevContainerFeature(
        name="ghcr.io/devcontainers/features/docker-outside-of-docker:1",
        version="latest",
    )
)
devContainer.add_tasks(Task(name="synth", exec="npx -y projen"))
project.synth()
