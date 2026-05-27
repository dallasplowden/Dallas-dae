extends CharacterBody2D

var currentspeed = 400

func _physics_process(delta: float) -> void:	
	var direction := Input.get_axis("ui_left", "ui_right")
	if direction:
		velocity.x = direction * currentspeed
	else:
		velocity.x = move_toward(velocity.x, 0, currentspeed)
	move_and_slide()
