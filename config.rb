# VM Config
$ssh_user = "vagrant"
$vcpus = "4"
$vmem  = "4096"

# Synced Folders
$host_folder = "."
$vm_folder = "/home/vagrant/dev"

# HyperV Specific
$centos8hv_box = "hauptj/CentOS8Base"
$centos8hv_box_ver = "0.0.3"
$hv_vm_name = "Centos8HVK8s"
$hv_net_bridge = "Default Switch"
$hv_max_mem = "6144"

# VB Specific
$centos8vb_box = "generic/centos8"
$centos8vb_box_ver = "3.0.10"
$vb_vm_name = "Centos8VBK8s"
$vb_private_ip = "192.168.123.123"