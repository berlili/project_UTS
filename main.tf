terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "ubuntu" {
  name = "ubuntu:latest"
}

resource "docker_container" "server_uas_analitik" {
  name  = "server_uas_analitik"
  image = docker_image.ubuntu.image_id

  tty        = true
  stdin_open = true

  command = ["sleep", "infinity"]
}