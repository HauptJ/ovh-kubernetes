# -*- mode: ruby -*-
# vi: set ft=ruby :
# NOTE: Variable overrides are in ./config.rb
require "yaml"
require "fileutils"

# Use a variable file for overrides:
CONFIG = File.expand_path("config.rb")
if File.exist?(CONFIG)
  require CONFIG
end

Vagrant.configure("2") do |config|

  config.vm.define "centos8hv" do |centos8hv|
    centos8hv.vm.box = $centos8_box
    centos8hv.vm.box_version = $centos8_box_ver
    centos8hv.ssh.username = $ssh_user

    # NOTE: This is specific for my machine
    # Change bridge: $hv_net_bridge to the name of your
    # External V-Switch
    centos8hv.vm.network "public_network", bridge: $hv_net_bridge

  	centos8hv.vm.provider "hyperv" do |hv|
  		hv.vmname = $hv_vm_name
  		hv.cpus = $vcpus
  		hv.memory = $vmem
      # HV max memory
      hv.maxmemory = $hv_max_mem
      # Faster cloning and uses less disk space
      hv.linked_clone = false
  	end

    # Provision box
    centos8hv.vm.provision "file", source: "ansible", destination: "/tmp/ansible"

    centos8hv.vm.provision "shell", path: "ansible/ansible.sh"
  end

  config.vm.define "centos8vb" do |centos8vb|
    centos8vb.vm.box = $centos8_box
    centos8vb.vm.box_version = $centos8_box_ver
    centos8vb.ssh.username = $ssh_user
    centos8vb.vm.synced_folder $host_folder, $vm_folder

    centos8vb.vm.network "private_network", ip: $vb_private_ip

    centos8vb.vm.provider "virtualbox" do |vb|
      vb.name = $vb_vm_name
      vb.cpus = $vcpus
      vb.memory = $vmem
      # Faster cloning and uses less disk space
      vb.linked_clone = false
    end

    # Provision box
    centos8vb.vm.provision "file", source: "ansible", destination: "/tmp/ansible"

    centos8vb.vm.provision "shell", path: "ansible/ansible.sh"
  end
  
end

