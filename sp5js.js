<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
    <style>
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }
      canvas {
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
    <script>
      let snake;
      let scl = 20;
      let food;

      function setup() {
        createCanvas(400, 400);
        snake = new Snake();
        frameRate(10);
        pickLocation();
      }

      function pickLocation() {
        let cols = floor(width / scl);
        let rows = floor(height / scl);
        food = createVector(floor(random(cols)), floor(random(rows)));
        food.mult(scl);
      }

      function mousePressed() {
        snake.total++;
      }

      function draw() {
        background(0);

        if (snake.eat(food)) {
          pickLocation();
        }
        snake.death();
        snake.update();
        snake.show();

        fill(255, 0, 100);
        rect(food.x, food.y, scl, scl);
      }

      function keyPressed() {
        if (keyCode === UP_ARROW) {
          snake.dir(0, -1);
        } else if (keyCode === DOWN_ARROW) {
          snake.dir(0, 1);
        } else if (keyCode === RIGHT_ARROW) {
          snake.dir(1, 0);
        } else if (keyCode === LEFT_ARROW) {
          snake.dir(-1, 0);
        }
      }

      function Snake() {
        this.x = 0;
        this.y = 0;
        this.xspeed = 1;
        this.yspeed = 0;
        this.total = 0;
        this.tail = [];

        this.eat = function(pos) {
          let d = dist(this.x, this.y, pos.x, pos.y);
          if (d < 1) {
            this.total++;
            return true;
          } else {
            return false;
          }
        };

        this.dir = function(x, y) {
          this.xspeed = x;
          this.yspeed = y;
        };

        this.death = function() {
          for (let i = 0; i < this.tail.length; i++) {
            let pos = this.tail[i];
            let d = dist(this.x, this.y, pos.x, pos.y);
            if (d < 1) {
              this.total = 0;
              this.tail = [];
            }
          }
        };

        this.update = function() {
          if (this.total === this.tail.length) {
            for (let i = 0; i < this.tail.length - 1; i++) {
              this.tail[i] = this.tail[i + 1];
            }
          }
          this.tail[this.total - 1] = createVector(this.x, this.y);

          this.x = this.x + this.xspeed * scl;
          this.y = this.y + this.yspeed * scl;

          this.x = constrain(this.x, 0, width - scl);
          this.y = constrain(this.y, 0, height - scl);
        };

        this.show = function() {
          fill(255);
          for (let i = 0; i < this.tail.length; i++) {
            rect(this.tail[i].x, this.tail[i].y, scl, scl);
          }
          rect(this.x, this.y, scl, scl);
        };
      }
    </script>
  </body>
</html>
