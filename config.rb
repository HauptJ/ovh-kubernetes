# VM Config
$ssh_user = "vagrant"
$vcpus = "4"
$vmem  = "4096"

# HyperV Specific
$hv_net_bridge = "LANBridge"
$hv_max_mem = "6144"

# Centos 8 Specific
$centos8_box = "generic/centos8"
$centos8_box_ver = "1.9.38"

# Fedora 29 Specific
$fedora29_box = "roboxes/fedora29"
$fedora29_box_ver = "2.0.2"
$fedora29_vmname = "Fedora29HVK8s"

# Fedora 31 Specific
$fedora30_box = "roboxes/fedora30"
$fedora30_box_ver = "2.0.6"
$fedora30_vmname = $fedora29_vmname = "Fedora30HVK8s"