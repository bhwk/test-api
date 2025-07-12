output "container_id" {
  description = "ID of the docker container"
  value = docker_container.fastapi.id
}

output "image_id" {
  description = "ID of the docker image"
  value = docker_image.fastapi.id
}
