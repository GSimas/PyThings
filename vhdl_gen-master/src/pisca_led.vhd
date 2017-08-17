------------------------------------------------------
-- Name : Gustavo
-- Created at : 15-08-2017 15:29
------------------------------------------------------

--Libraries and use clauses
 
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity PISCA-ESTRELINHA is
  port (
    sysclk  : in std_logic;
    
    reset_n  : in std_logic;
    
    enable  : in std_logic;
    
    leds  : out std_logic_vector(15 downto 0);
   
    );
end PISCA-ESTRELINHA;

------------------------------------------------------

architecture rtl of PISCA-ESTRELINHA is
  type STATE_MACHINE_TYPE is (S0,S1,S2,S3);

  attribute SYN_ENCODING : string;
  attribute SYN_ENCODING of STATE_MACHINE_TYPE : type is "safe";

  signal state      : STATE_MACHINE_TYPE;
  signal state_next : STATE_MACHINE_TYPE;

  signal _reg
  signal _next
  signal timer_reg : std_logic_vector(15 downto 0);
  signal timer_next : std_logic_vector(15 downto 0);
  signal _reg
  signal _next
  signal leds_i_reg : std_logic_vector(15 downto 0);
  signal leds_i_next : std_logic_vector(15 downto 0);

begin

-- Sequential process 
  process(sysclk, ) is
  begin
    if ( = '0') then
      state <= S0;
    elsif rising_edge(sysclk) then
      leds_i_reg <= leds_i_next;
      _reg <= _next;
      timer_reg <= timer_next;
      state <= state_next;
    end if;
  end process;

-- Combinational process 
  process(state, leds_i_reg, _reg, timer_reg) is
  begin
    leds_i_next <= leds_i_reg;
    _next <= _reg;
    timer_next <= timer_reg;
    state_next <= state;
  
    case state is

      when S0 =>
          null;
      when S1 =>
          null;
      when S2 =>
          null;
      when S3 =>
          null;
      when OTHERS =>
          null;
    end case;
  end process;


end rtl;