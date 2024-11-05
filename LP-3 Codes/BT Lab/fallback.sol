// SPDX-License-Identifier: MIT

pragma solidity >=0.8.2 <0.9.0;

contract Fback {
    // Declaring the state variable
    uint x;

    // Mapping of addresses to their balances
    mapping(address => uint) balance;

    // Creating a constructor
    constructor() {
        // Set x to default value of 10
        x = 10;
    }

    // Function to set x to the value sent
    function setX(uint _x) public returns (bool) {
        x = _x;
        return true;
    }

    // Fallback function to receive Ether and update the balance mapping
    fallback() external payable {
        balance[msg.sender] += msg.value;
    }

    // Optional receive function for plain Ether transfers (without data)
    receive() external payable {
        balance[msg.sender] += msg.value;
    }
}

// Creating the sender contract
contract Sender {
    function transfer() public payable {
        // Address of Fback contract
        address payable _receiver = payable(0xbcD310867F1b74142c2f5776404b6bd97165FA56);
        
        // Transfers 100 Ether to the above contract
        _receiver.transfer(100 ether);
    }
}
