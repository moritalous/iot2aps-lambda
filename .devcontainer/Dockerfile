# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.231.2/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use hirsuite or bionic on local arm64/Apple Silicon): hirsute, focal, bionic
ARG VARIANT="hirsute"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN apt-get update && apt-get install -y python3.9 python3-pip

# Install AWS CLI
RUN curl -L "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscli-exe.zip" && \
    unzip /tmp/awscli-exe.zip -d /tmp && \
    /tmp//aws/install && \
    rm -rf /tmp/aws/install && \
    rm -rf /tmp/awscli-exe.zip

# Install AWS SAM CLI
RUN curl -L "https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip" -o "/tmp/aws-sam-cli.zip" && \
    unzip /tmp/aws-sam-cli.zip -d /tmp/sam-installation && \
    /tmp/sam-installation/install && \
    rm -rf /tmp/sam-installation && \
    rm -rf /tmp/aws-sam-cli.zip

