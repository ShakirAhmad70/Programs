import java.awt.Color;
import java.awt.Graphics;

public class Balloon {
    private int x;              // x-coordinate of the balloon
    private int y;              // y-coordinate of the balloon
    private int diameter;       // diameter of the balloon

    public Balloon() {
        x = 200;                // initial x-coordinate
        y = 200;                // initial y-coordinate
        diameter = 50;          // initial diameter
    }

    public void grow() {
        diameter += 10;         // increase the diameter by 10 pixels
    }

    public void shrink() {
        if (diameter > 10) {
            diameter -= 10;     // decrease the diameter by 10 pixels (if it's greater than 10)
        }
    }

    public void moveLeft() {
        x -= 10;                // move the balloon 10 pixels to the left
    }

    public void moveRight() {
        x += 10;                // move the balloon 10 pixels to the right
    }

    public void display(Graphics g) {
        g.setColor(Color.RED);                      // set the color of the balloon to red
        g.fillOval(x, y, diameter, diameter);        // draw a filled oval representing the balloon
    }
}
