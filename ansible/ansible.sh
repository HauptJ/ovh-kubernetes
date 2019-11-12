#!/bin/bash -eux

pushd /tmp

sudo dnf -y install ansible

pushd /tmp/ansible

ansible-playbook -i hosts playbook.yml --skip-tags "open_ports,close_ports"

popd

popd