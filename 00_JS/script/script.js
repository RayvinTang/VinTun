document.addEventListener('DOMContentLoaded', () => {

	let canvas = document.getElementById("canvas");
	let ctx = canvas.getContext("2d");

	let score = 0;

	// console.log(canvas.width, canvas.height);
	const blockSize = 20;
	const column = canvas.width / blockSize;
	const row = column;

	const border = {

		color : "Black",
		size : blockSize,
		width : canvas.width,
		height : canvas.height,

		draw : function() {

			ctx.fillStyle = this.color;
			const top = ctx.fillRect(0, 0, this.width, this.size);
			const right = ctx.fillRect(this.width-this.size, 0, this.size, this.height);

			const bottom = ctx.fillRect(0, this.height-this.size, this.width, this.size);
			const left = ctx.fillRect(0, 0, this.size, this.height);

		}
	}

	let scoreText = {
		font : "20px Courier",
		color : "White",
		align : "left",
		baseline : "top",

		draw : function () {
			const x = 0;
			const y = 0;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Score : ${score}`, x, y);
		}
	}

	const gameOverText = {
		font : "60px Courier",
		color : "White",
		align : "center",
		baseline : "middle",

		draw : function () {
			const x = canvas.width/2;
			const y = canvas.height/2;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Game Over`, x, y);
		}
	}

	class Block {

		constructor(row, column){ //(y, x)
			this.row = row;
			this.column = column;

			this.size = blockSize;
		}

		circle(x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			// ctx.stroke();
			if (isFilled) {
				ctx.fillStyle = color;
				ctx.fill();
			}
		}

		drawSquare(color){
			let x = this.column * this.size;
			let y = this.row * this.size;
			this.color = color;

			ctx.fillStyle = this.color;
			ctx.fillRect(x, y, this.size, this.size);
		}

		drawCircle(color){
			let x = this.column * this.size + this.size/2;
			let y = this.row * this.size + this.size/2;
			this.color = color;

			this.circle(x, y, this.size/2, this.color, true);
		}

	}

	class Snake {

		constructor(){
			this.segments = [
				new Block(7, 5), // head
				new Block(6, 5),
				new Block(5, 5) // tail
			]
			this.direction = "right";
			this.nextDirection = "right";
		}

		draw(){
			this.segments.forEach((segment) => {
				segment.drawSquare("Blue");
			});

		}

		setDirection(newDirection){
			if (this.direction === "right" && newDirection === "left") return;
			if (this.direction === "left" && newDirection === "right") return;
			if (this.direction === "up" && newDirection === "down") return;
			if (this.direction === "down" && newDirection === "up") return;

			console.log(newDirection);
			this.nextDirection = newDirection;
		}

	}

	class Apple {

		constructor(){
			this.block = new Block(0,0);
			this.move();
		}

		draw(){
			this.block.drawCircle("Green");
		}

		move(){
			let randomRow = Math.floor(Math.random() * (row-2)) + 1;
			let randomColumn = Math.floor(Math.random() * (column-2)) + 1;
			this.block.row = randomRow;
			this.block.column = randomColumn;
		}


	}


	border.draw();
	scoreText.draw();

	let snake = new Snake();
	snake.draw();

	let apple = new Apple();
	apple.draw();

	// gameOverText.draw();
	// document.querySelector("body").onkeydown = (event) => {
	// 	console.log(event.code);
	// }
	// Jquery
	// $('body').keydown( (event) => {
	// 	console.log(event.keyCode);
	// })

	document.addEventListener('keydown', () => {
		// console.log(event.code);
		switch (event.code) {
			case "KeyW":
				snake.setDirection("up");
				break;
			case "KeyS":
				snake.setDirection("down");
				break;
			case "KeyA":
				snake.setDirection("left");
				break;
			case "KeyD":
				snake.setDirection("right");
				break;
			default:
				console.log("undefined");

		}
	})

})
