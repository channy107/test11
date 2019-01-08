pragma solidity ^0.4.25;

contract Contents {
    string contentsWriter;
    uint32 contentsPrice;
    string public contentsHashdata;

    constructor (string name, uint32 price, string hash) public {
        contentsWriter = name;
        contentsPrice = price;
        contentsHashdata = hash;
    }
    
    function getContentsWriter() public view returns (string) {
        return contentsWriter;
    }

    function getContentsPrice() public view returns (uint32) {
        return contentsPrice;
    }

    function getcontentsHashdata() public view returns (string) {
        return contentsHashdata;
    }

}

contract ContentsMaster {
    mapping (address => Contents) public contents;
    address[] private addressList;

    event EventAddContents(string name);

    function addContents(string name, uint32 price, string hash) public {
        Contents c = new Contents(name, price, hash);
        addressList.push(address(c));
        contents[address(c)] = c;

        emit EventAddContents(name);
    }

    function getContentsAddressList() public view returns (address[]
    contentsAddressList) {
        contentsAddressList = addressList;
    }
}
	