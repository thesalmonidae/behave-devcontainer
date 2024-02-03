ARG     ROCKYLINUX_VERSION
FROM    rockylinux:${ROCKYLINUX_VERSION}

ARG     DOCKER_GROUP_ID
ARG     NON_ROOT_USER

ARG     AIOHTTP_VERSION
ARG     BEHAVE_VERSION
ARG     HELM_VERSION
ARG     K9S_VERSION
ARG     KUBECTL_VERSION
ARG     KUBERNETES_VERSION
ARG     PYTHON_VERSION

RUN     adduser -m ${NON_ROOT_USER} &&\
        microdnf install -y dnf &&\
        dnf install -y 'dnf-command(config-manager)' &&\
        dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo &&\
        dnf install -y \
                bzip2-devel \
                curl \
                docker-ce-cli \
                libffi-devel \
                make \
                openssl-devel &&\
        groupmod -g ${DOCKER_GROUP_ID} docker &&\
        usermod -aG docker ${NON_ROOT_USER} &&\
        dnf groupinstall -y "Development Tools" &&\
        curl -LO https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz &&\
        tar -xzf Python-${PYTHON_VERSION}.tgz &&\
        cd Python-${PYTHON_VERSION} &&\
        ./configure --enable-optimizations &&\
        make install &&\
        cd .. &&\
        rm Python-${PYTHON_VERSION}.tgz &&\
        python3 -m pip install \
                aiohttp==${AIOHTTP_VERSION} \
                behave==${BEHAVE_VERSION} \
                kubernetes==${KUBERNETES_VERSION} &&\
        curl -LO https://dl.k8s.io/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl &&\
        chmod +x kubectl &&\
        mv kubectl /usr/local/bin/kubectl &&\
        curl -LO https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz &&\
        tar -zxvf helm-v${HELM_VERSION}-linux-amd64.tar.gz &&\
        mv linux-amd64/helm /usr/local/bin/helm &&\
        rm helm-v${HELM_VERSION}-linux-amd64.tar.gz &&\
        curl -LO https://github.com/derailed/k9s/releases/download/v${K9S_VERSION}/k9s_Linux_amd64.tar.gz &&\
        tar -zxf k9s_Linux_amd64.tar.gz &&\
        mv k9s /usr/local/bin/k9s

WORKDIR /home/${NON_ROOT_USER}

USER    ${NON_ROOT_USER}
