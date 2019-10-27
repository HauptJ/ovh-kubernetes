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

  config.vm.define "centos8" do |centos8|
    centos8.vm.box = $centos8_box
    centos8.vm.box_version = $centos8_box_ver
    centos8.ssh.username = $ssh_user

  	centos8.vm.provider "hyperv" do |hv|
  		hv.vmname = $centos8_vmname
  		# With nested virtualization, at least 2 CPUs are needed.
  		hv.cpus = $vcpus
  		# With nested virtualization, at least 4GB of memory is needed.
  		hv.memory = $vmem
      # Faster cloning and uses less disk space
      hv.differencing_disk = true
  	end

    # Provision box

  end