import discord
import gpt_2_simple as gpt2
from discord.ext import commands

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')

def generateText(prefix):
	gen_file = 'gpt2_gentext_test.txt'
	gpt2.generate_to_file(sess,
    destination_path=gen_file,
    length=15,
    temperature=0.7,
    prefix = prefix,
    nsamples=1,
    batch_size=1,
    include_prefix = False
    )

def readOutput():
	with open('gpt2_gentext_test.txt', encoding = 'utf8') as f:
  	lines = f.readlines()
  	output = ''
  	for line in lines:
  		output += line
  		output += ' '
  	return output


TOKEN = #Your Discord Env Token here
GUILD = #Your server name here

client = commands.Bot(command_prefix = './')

@client.event
async def on_ready():
	print ("Ready")

@client.command()
async def royce(ctx, *args):
	generateText(args)
	output = readOutput
	await ctx.send(output)

client.run(TOKEN)

