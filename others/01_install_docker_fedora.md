# Installing Docker of Fedora 32

Commands:
```bash
# add repo and install CE edition

sudo dnf -y install dnf-plugins-core
sudo dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io

# CGroups Backwards Compatibility
sudo grubby --update-kernel=ALL --args="systemd.unified_cgroup_hierarchy=0"
  # <reboot after this>

# Run hello-world to confirm install
sudo systemctl start docker
sudo docker run hello-world

# Setup a non-root user to use docker
sudo usermod -aG docker jay
newgrp docker

# Run from non-root user
docker run hello-world
```