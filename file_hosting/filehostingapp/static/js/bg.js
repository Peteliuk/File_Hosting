(function() {
	
	let canvas = document.createElement('canvas'),
	ctx = canvas.getContext('2d'),
	w = canvas.width = innerWidth,
	h = canvas.height = innerHeight,
	particles = [],
	properties = {
		bgColor 			: 'rgba(17,17,19,1)',
		particleColor		: 'rgba(10,255,10,.8)',
		particleRadius		: 3,
		particleCount		: 30,
		particleMaxVelocity	: .2,
		lineLength			: 150,
		particleLife		: 30
	};

	document.querySelector('body').appendChild(canvas);

	window.onresize = function(){
		w = canvas.width = innerWidth,
		h = canvas.height = innerHeight;
	}

	class Particle {
		constructor(){
			this.x = Math.random()*w;
			this.y = Math.random()*h;
			this.velicityX = Math.random()*(properties.particleMaxVelocity*2)-properties.particleMaxVelocity;
			this.velicityY = Math.random()*(properties.particleMaxVelocity*2)-properties.particleMaxVelocity;
			this.life = Math.random()*properties.particleLife*60;
		}

		position(){
			this.x + this.velicityX > w && this.velicityX > 0 || this.x + this.velicityX < 0 && this.velicityX < 0 ? 
			this.velicityX *= -1 : this.velicityX;
			this.y + this.velicityY > h && this.velicityY > 0 || this.y + this.velicityY < 0 && this.velicityY < 0 ? 
			this.velicityY *= -1 : this.velicityY;
			this.x += this.velicityX;
			this.y += this.velicityY;
		}

		reDraw(){
			ctx.beginPath();
			ctx.arc(this.x, this.y, properties.particleRadius, 0, Math.PI*2);
			ctx.closePath();
			ctx.fillStyle = properties.particleColor;
			ctx.fill();
		}

		reCalcLife(){
			if(this.life < 1){
				this.x = Math.random()*w;
				this.y = Math.random()*h;
				this.velicityX = Math.random()*(properties.particleMaxVelocity*2)-properties.particleMaxVelocity;
				this.velicityY = Math.random()*(properties.particleMaxVelocity*2)-properties.particleMaxVelocity;
				this.life = Math.random()*properties.particleLife*60;
			}
			this.life--;
		}
	}

	function reDrawBackground(){
		ctx.fillStyle = properties.bgColor;
		ctx.fillRect(0,0,w,h);
	}

	function drawLines(){
		let x1, y1, x2, y2, length, opacity;
		for(let i in particles){
			for(let j in particles){
				x1 = particles[i].x;
				y1 = particles[i].y;
				x2 = particles[j].x;
				y2 = particles[j].y;
				length = Math.sqrt((x2 - x1)**2 + (y2 - y1)**2);
				if(length < properties.lineLength){
					opacity = 1 - length/properties.lineLength;
					ctx.lineWidth = '0.5';
					ctx.strokeStyle = `rgba(10,255,10,${opacity})`;
					ctx.beginPath();
					ctx.moveTo(x1,y1);
					ctx.lineTo(x2,y2);
					ctx.closePath();
					ctx.stroke();
				}
			}
		}
	}

	function reDrawParticles(){
		for(let i in particles){
			particles[i].reCalcLife();
			particles[i].position();
			particles[i].reDraw();
		}
	}

	function loop(){
		reDrawBackground();
		reDrawParticles();
		drawLines();
		requestAnimationFrame(loop);
	}

	function init(){
		for (let i = 0; i < properties.particleCount; i++) {
			particles.push(new Particle);
		}
		loop();
	}

	init();

}())