#!/usr/bin/ruby -w

class Customer
    @@no_of_customer=0
    def initialize(id, name, addr)
        @cust_id = id
        @cust_name=name
        @cust_addr=addr
        @@no_of_customer = @@no_of_customer + 1
    end
    def print()
        puts "no_of_customer: ", @@no_of_customer
    end
end

cust1=Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
cust2=Customer.new("2", "Poul", "New Empire road, Khandala")
cust2.print()

