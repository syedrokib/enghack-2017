package app.srrna.sms;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
Button send;

    TextView SMS;
    EditText dest;
    String var="43.4704675,-80.543411";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        send= (Button) findViewById(R.id.button);

        dest= (EditText) findViewById(R.id.editText);

        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SmsManager smsManager=SmsManager.getDefault();
                String destination=dest.getText().toString();
                smsManager.sendTextMessage("2898092772",null,var+" \n"+destination ,null,null);

                Toast.makeText(MainActivity.this, "Destination Sent please wait...", Toast.LENGTH_LONG).show();
                Toast.makeText(MainActivity.this, "Please check your SMS inbox.", Toast.LENGTH_SHORT).show();

            }
        });






    }



}
