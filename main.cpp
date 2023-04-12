#include "mbed.h"
#include "SocketAddress.h"
#include "EthernetInterface.h"
#include <cstdlib>
#include<string>

#define DELTA 200
#define DELTAMOTOR 0.2
#define DELTATEMPS 0.1
#define DELTAMOTORCORRECTION 0.04
#define POWER_LIMIT 0.8

//Serial pc(USBTX, USBRX);
PwmOut myled(LED1);

PwmOut pwmDroite(D10);
DigitalOut dirDroite(D8);
PwmOut pwmGauche(D9);
DigitalOut dirGauche(D7);

float power_Droite = 0.0;
float power_Gauche = 0.0;
float power_Droite_Correctif = 0.0;
float power_Gauche_Correctif = 0.0;

void wait(float s){
    wait_us((int)s*1000000);
    return;
}

/*Attribution d'une adresse ip pour la carte, le mask du réseau, et la passerelle*/
const char* ipAdresse = "169.254.23.213";
const char* ipMask = "255.255.0.0";
const char* ipGetway = "192.168.43.1";
const char* myAddress = "169.254.23.212";

/*La classe Ethernet*/
EthernetInterface eth;

void testMotor(){
    pwmDroite.period_us(1000);
    pwmGauche.period_us(1000);
    pwmDroite.pulsewidth_us(900);
    pwmGauche.pulsewidth_us(900);
    dirDroite=0;
    dirGauche=1;
    wait(2);
    pwmDroite.pulsewidth_us(0);
    pwmGauche.pulsewidth_us(0);
    wait(.05);

}


void setupEth(){
  /*Initialiser la connection */
  eth.set_network(ipAdresse, ipMask, ipGetway);
  eth.connect(); //Crée la connection
}

int main(void){
    // testMotor();

    wait(1);
    setupEth();

    SocketAddress monAdresse;  //La socket de la carte Nucleo

    eth.get_ip_address(&monAdresse); //Attribuer la socket à la connection ethernet

    SocketAddress pcAdresse; //La socket du pc
    eth.gethostbyname(myAddress, &pcAdresse);

    eth.ethInterface();

    UDPSocket sock; //Une socket UDP pour le transport (couche transport) .
    sock.open(&eth); //Associer la socket UDP a la connection eth.

    pcAdresse.set_port(8080); //Le port de connection.

    char out_buffer[] = "ready"; ///Le message a envoyer au pc
    char in_data[1];

    sock.sendto(pcAdresse, out_buffer, sizeof(out_buffer));
    wait(0.1);
    while (1){
      sock.recvfrom(&pcAdresse, &in_data, sizeof(in_data));
      char message[] = "receive";
      sock.sendto(pcAdresse, message, sizeof(message));
      wait(0.1);
      sock.sendto(pcAdresse, in_data, sizeof(in_data));
      wait(0.1);
      if(in_data[0]=='a'){

        pwmDroite.pulsewidth_us(0);
        pwmGauche.pulsewidth_us(800);
      }
      if(in_data[0]=='z'){
        pwmDroite.pulsewidth_us(800);
        pwmGauche.pulsewidth_us(0);
      }
      if(in_data[0]=='e'){
        pwmDroite.pulsewidth_us(0);
        pwmGauche.pulsewidth_us(0);
      }
      if(in_data[0]=='s'){
        pwmDroite.pulsewidth_us(0);
        pwmGauche.pulsewidth_us(0);
      }
  }

}
