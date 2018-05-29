import scalamain.Main;
import py4j.GatewayServer;

public class Hello{
    public void smain() {
      Main.main();
    }

    public static void main(String[] args) {
        Hello hello = new Hello();
        GatewayServer server = new GatewayServer(hello);
        server.start();
    }

}
