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
  		hv.vmname = "Centos8HVK8s"
  		# With nested virtualization, at least 2 CPUs are needed.
  		hv.cpus = $vcpus
  		# With nested virtualization, at least 4GB of memory is needed.
  		hv.memory = $vmem
      # HV max memory
      hv.maxmemory = $hv_max_mem
      # Faster cloning and uses less disk space
      hv.linked_clone = true
  	end

    # Provision box
    centos8hv.vm.provision "file", source: "ansible", destination: "/tmp/ansible"

    centos8hv.vm.provision "shell", path: "ansible/ansible.sh"
  end

  config.vm.define "fedora29hv" do |fedora29hv|
    fedora29hv.vm.box = $fedora29_box
    fedora29hv.vm.box_version = $fedora29_box_ver
    fedora29hv.ssh.username = $ssh_user

    # NOTE: This is specific for my machine
    # Change bridge: $hv_net_bridge to the name of your
    # External V-Switch
    fedora29hv.vm.network "public_network", bridge: $hv_net_bridge

  	fedora29hv.vm.provider "hyperv" do |hv|
  		hv.vmname = "Fedora29HVK8s"
  		# With nested virtualization, at least 2 CPUs are needed.
  		hv.cpus = $vcpus
  		# With nested virtualization, at least 4GB of memory is needed.
  		hv.memory = $vmem
      # HV max memory
      hv.maxmemory = $hv_max_mem
      # Faster cloning and uses less disk space
      hv.linked_clone = true
  	end

    # Provision box
    fedora29hv.vm.provision "file", source: "ansible", destination: "/tmp/ansible"

    fedora29hv.vm.provision "shell", path: "ansible/ansible.sh"
  end

end

