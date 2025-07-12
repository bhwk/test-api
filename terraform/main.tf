terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "fastapi" {
  name = "testapi"
  build {
    context = "${path.module}/.."
  }
}

resource "docker_container" "fastapi" {
  name = var.container_name
  image = docker_image.fastapi.name
  ports {
    internal = 8000
    external = 4040
  }
}

