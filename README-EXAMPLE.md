# Run an example

This README will throw you onto the execution of an example topology of Fabric network running on top of umbra simulator.

## Prerequisites

Let's spin up a VM with all the required dependencies installed. We will use Vagrant to do so.

```bash
vagrant up
vagrant status
vagrant ssh umbra_virtualbox
```

Now we are inside the VM. Let's clone the repository and install the dependencies.

```bash
sudo git clone https://github.com/n-elia/hyperledger-umbra
cd hyperledger-umbra
sudo make install-fabric
sudo make install-iroha
```

> Note that we need to execute `sudo make install-iroha` because there is a bug that prevents the execution of the Fabri experiments if the Iroha dependencies are not installed.

## Run the example

Let's run the example topology of Fabric network.

```bash
cd examples
sudo python3 fabric/local-2orgs.py

sudo umbra-cli --uuid umbra-cli --address 127.0.0.1:9988 --debug --source /tmp/umbra/fabric/
```

Now we are inside the umbra-cli. Let's load the configuration and install the environments.

```bash
load /tmp/umbra/fabric/local-2orgs.json
install
start
begin
```


