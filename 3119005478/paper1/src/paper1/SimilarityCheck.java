package paper1;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class SimilarityCheck {
	Map<Character,int[]>vectorMap = new HashMap<Character,int[]>();
	int[] tempArray = null;
	public SimilarityCheck(String source,String target) {
		for(Character sch:source.toCharArray()) {
			if(vectorMap.containsKey(sch)) {
				vectorMap.get(sch)[0]++;
			}
			//调用Vector的构造函数将字符转换为向量
			else {
				tempArray = new int[2];
				tempArray[0] = 1;
				tempArray[1] = 0;
				vectorMap.put(sch,tempArray);
			}
		}
		for(Character tch:target.toCharArray()) {
			if(vectorMap.containsKey(tch)) {
				vectorMap.get(tch)[1]++;
			}
			else {
				tempArray = new int[2];
				tempArray[0] = 0;
				tempArray[1] = 1;
				vectorMap.put(tch,tempArray);
			}
		}
	}	//余弦相似度
	public double sim() {
		double result = 0;
		result = pointMulti(vectorMap)/sqrtMulti(vectorMap);
		return result;
	}//平方和
	private double squares(Map<Character,int[]>paramMap) {
		double result1 = 0;
		double result2 = 0;
		Set<Character>keySet = paramMap.keySet();
			for(Character character:keySet) {
				int temp[] = paramMap.get(character);
				result1+=(temp[0]*temp[1]);
				result2+=(temp[1]*temp[1]);
			}
			return result1*result2;
		}//点乘法
		private double pointMulti(Map<Character,int[]>paramMap) {
			double result = 0;
			Set<Character>keySet = paramMap.keySet();
			for(Character character:keySet) {
				int temp[] = paramMap.get(character);
				result+=(temp[0]*temp[1]);
			}
			return result;
		}
		private double sqrtMulti(Map<Character,int[]>paramMap) {
			double result = 0;
			result = squares(paramMap);
			result = Math.sqrt(result);
			return result;
		}
		public static void main(String[] args) throws IOException {
			Path path1 = Paths.get("D:/origin.txt");
			Path path2 = Paths.get("D:/Plagiarism.txt");//读取文件	
			File file = new File("D:/answer.txt");//写入文件
			FileWriter fileWriter = new FileWriter(file);
			byte[] data;
			try {
				data = Files.readAllBytes(path1);
				String s1= new String(data, "utf-8");
				data = Files.readAllBytes(path2);
				String s2=new String(data, "utf-8");
				SimilarityCheck t2 =new SimilarityCheck(s1,s2);	
				double sim = t2.sim();
			    System.out.println("相似度为"+String.format("%.2f", sim));//保留小数点后两位
			    fileWriter.write("相似度为"+String.format("%.2f", sim));
			    fileWriter.close();

			} catch (Exception e) {
				System.out.println("读取文件内容操作出错");
				fileWriter.write("读取文件内容操作出错");
			    fileWriter.close();
				e.printStackTrace();
			}			
		}}

		
	
