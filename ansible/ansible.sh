#!/bin/bash -eux

pushd /tmp

sudo dnf -y install git ansible

pushd /tmp/ansible

ansible-playbook -i hosts playbook.yml

popd

popd