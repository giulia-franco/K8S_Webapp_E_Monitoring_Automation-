# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Rocky Linux 9 VM Setup
    config.vm.define "vm" do |vm|
      config.vm.box = "generic/rocky9"
      config.vm.box_version = "4.3.12"
      config.vm.hostname = "vm-rocky9"
  # Network settings and IP assignment
      config.vm.network "private_network", ip: "192.168.168.7"
  # VM resources
      config.vm.provider "virtualbox" do |vb|
        vb.memory = "4096"
        vb.cpus = 4
      end
  # Provision Ansible 
      config.vm.provision "ansible" do |ansible|
        ansible.compatibility_mode = "1.8"
        ansible.playbook = "provisioning/cipia4.yml"
      end
    end 
  end