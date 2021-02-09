// import javax.xml.bind.annotation.adapters.HexBinaryAdapter;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;

public class SimpleReceiver1 extends Thread{

    private ServerSocket ss;
    static AtomicBoolean allTransfersCompleted = new AtomicBoolean(false);
    static String baseDir = "/home/cc/received_files/";

    static long totalTransferredBytes = 0L;
    static long totalChecksumBytes = 0L;
    long INTEGRITY_VERIFICATION_BLOCK_SIZE = 256 *1024 * 1024;

    boolean debug = false;
    long startTime;
   	int yy  = 1;
	int FileCount;

    static LinkedBlockingQueue<Item> items = new LinkedBlockingQueue<>(10000);

    class Item {
        byte[] buffer;
        int length;

        public Item(byte[] buffer, int length){
            this.buffer = Arrays.copyOf(buffer, length);
            this.length = length;
        }
    }

    public class FiverFile {
        public FiverFile(File file, long offset, long length) {
            this.file = file;
            this.offset = offset;
            this.length = length;
        }
        File file;
        Long offset;
        Long length;
    }


    public SimpleReceiver1(int port) {
        try {
            ss = new ServerSocket(port);
           
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() {
        while (true) {
            try {
                Socket clientSock = ss.accept();
                // clientSock.setSoTimeout(10000);
                System.out.println("Connection established from  " + clientSock.getInetAddress());
                saveFile(clientSock);
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    private void saveFile(Socket clientSock) throws IOException, InterruptedException {


        // startTime = System.currentTimeMillis();
        DataInputStream dataInputStream  = new DataInputStream(clientSock.getInputStream());
        INTEGRITY_VERIFICATION_BLOCK_SIZE = dataInputStream.readLong();

        allTransfersCompleted.set(false);
        totalTransferredBytes = 0L;
        totalChecksumBytes = 0L;

        // long init2 = System.currentTimeMillis();

        
        byte[] buffer = new byte[128 * 1024];
        while(true) {
            String fileName = dataInputStream.readUTF();
            long offset = dataInputStream.readLong();
            long fileSize = dataInputStream.readLong();
		    FileCount = dataInputStream.readInt();
            RandomAccessFile randomAccessFile = new RandomAccessFile(baseDir + fileName, "rw");

            if (offset > 0) {
                randomAccessFile.getChannel().position(offset);
            }
            long remaining = fileSize;
            int read = 0;
            // long transferStartTime = System.currentTimeMillis();
            while (remaining > 0) {
                read = dataInputStream.read(buffer, 0, (int) Math.min(buffer.length, remaining));
                if (read == -1)
                    break;
                totalTransferredBytes += read;
                remaining -= read;
                randomAccessFile.write(buffer, 0, read);
            }
            randomAccessFile.close();
            if (read == -1) {
                System.out.println("Read -1, closing the connection...");
                return;
            }
              
        	if (yy  == FileCount){
				// System.out.println("Checksum END File "  +  " time: " + (System.currentTimeMillis() - startTime) / 1000.0 + " seconds");
				System.out.println("FileCount: " + FileCount);
				// System.exit(0);
			}
			yy ++;

	   }

    }

    




    public static void main (String[] args) {
        if (args.length > 0) {
            baseDir = args[0];
        }
        SimpleReceiver1 fs = new SimpleReceiver1(50505);
        fs.start();
    }

}


