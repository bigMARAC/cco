library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity usertest is
end usertest;

architecture tb of usertest is
    signal En: std_logic := '1';
    signal E: std_logic_vector(1 downto 0) := "11";
    signal S: std_logic_vector(7 downto 0);
    
    component exercicio03 is port ( 
      En: in std_logic;
      E: in std_logic_vector(1 downto 0);
      S: out std_logic_vector(7 downto 0) );
    end component;
    
begin
DUT: exercicio03 port map (En, E, S);
    process
     constant period: time := 10 ns;
     begin
         for k in 1 to 4 loop
            wait for period;
            E <= E + '1';
         end loop;
         En <= '0';
         for k in 1 to 4 loop
            wait for period;
            E <= E + '1';
         end loop;
         wait;
    end process;    
end tb;
